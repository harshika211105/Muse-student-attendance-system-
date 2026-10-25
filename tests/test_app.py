import unittest
from app import add_student, mark_attendance


class AttendanceTests(unittest.TestCase):

    def test_add_student(self):
        students = {}
        self.assertTrue(add_student(students, "101", "Asha"))
        self.assertEqual(students["101"], "Asha")

    def test_duplicate_student(self):
        students = {"101": "Asha"}
        self.assertFalse(add_student(students, "101", "Riya"))

    def test_mark_present(self):
        records = {}
        self.assertTrue(
            mark_attendance(records, "101", "Present", "2026-10-25")
        )
        self.assertEqual(
            records[("101", "2026-10-25")], "Present"
        )

    def test_invalid_status(self):
        self.assertFalse(mark_attendance({}, "101", "Late"))


if __name__ == "__main__":
    unittest.main()
  
