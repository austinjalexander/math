"""Exercise packet boundaries and archive-integrity detection."""

import argparse
import importlib.util
import shutil
import tempfile
import unittest
from pathlib import Path

SPEC = importlib.util.spec_from_file_location(
    "agent_config", Path(__file__).resolve().parents[1] / "agent_config.py"
)
config = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(config)


class PacketTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        for name in (
            "AGENTS.md",
            "docs/agents/PROFILE.md",
            "docs/agents/tutoring.md",
            "docs/agents/module-structure.md",
            "docs/agents/math-and-code-style.md",
            ".agents/skills/tutor-session/SKILL.md",
            "PROGRESS.md",
            "EXTERNAL_COURSES.md",
            "GOALS.md",
            "docs/CURRICULUM.md",
            "STUDY_PLAN.md",
            "RESOURCES.md",
            "notes/topic/README.md",
            "notes/topic/notes.md",
            "notes/topic/problems.md",
            "notes/topic/solutions.md",
            "assessments/entry/diagnostic.md",
            "assessments/entry/solutions.md",
        ):
            path = self.root / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text("KEY_SENTINEL" if "solutions" in name else name)

    def packet(self, **kwargs):
        options = dict(skill="tutor-session", module=None, assessment=None, external_course=None)
        options.update(kwargs)
        return config.study_packet(self.root, argparse.Namespace(**options))

    def test_module_includes_prompts_but_excludes_key(self):
        packet = self.packet(module="notes/topic")
        self.assertIn("## Source: notes/topic/problems.md", packet)
        self.assertNotIn("## Source: notes/topic/solutions.md", packet)
        self.assertNotIn("KEY_SENTINEL", packet)

    def test_assessment_packet_has_no_lesson_content(self):
        packet = self.packet(assessment="assessments/entry/diagnostic.md")
        self.assertIn("## Source: assessments/entry/diagnostic.md", packet)
        self.assertNotIn("## Source: notes/topic", packet)
        self.assertNotIn("KEY_SENTINEL", packet)
        with self.assertRaises(ValueError):
            self.packet(module="notes/topic", assessment="assessments/entry/diagnostic.md")

    def test_reject_key_and_escape_paths(self):
        for value in ("../outside.md", "/etc/hosts", "notes/topic/solutions.md"):
            with self.subTest(value=value), self.assertRaises(ValueError):
                self.packet(assessment=value)
        link = self.root / "notes/topic/innocent.md"
        link.symlink_to(self.root / "notes/topic/solutions.md")
        with self.assertRaises(ValueError):
            self.packet(assessment="notes/topic/innocent.md")

    def test_module_symlink_cannot_import_answer_key(self):
        (self.root / "notes/topic/notes.md").unlink()
        (self.root / "notes/topic/notes.md").symlink_to("solutions.md")
        with self.assertRaises(ValueError):
            self.packet(module="notes/topic")

    def test_missing_file_fails_before_packet_return(self):
        (self.root / "notes/topic/problems.md").unlink()
        with self.assertRaises(OSError):
            self.packet(module="notes/topic")

    def test_archive_changes_are_detected(self):
        shutil.copytree(config.ROOT / "notebooks/archive", self.root / "notebooks/archive")
        self.assertEqual(config.archive_errors(self.root), [])
        with (self.root / "notebooks/archive/Definitions.ipynb").open("a") as stream:
            stream.write("\nchanged\n")
        self.assertTrue(
            any("checksum mismatch" in item for item in config.archive_errors(self.root))
        )


if __name__ == "__main__":
    unittest.main()
