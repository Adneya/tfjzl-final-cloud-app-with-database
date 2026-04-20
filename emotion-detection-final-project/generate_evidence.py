"""Generate task evidence files by running required commands."""

from __future__ import annotations

import os
import subprocess


def run_and_save(filename: str, command: str) -> None:
    """Run a shell command and save output plus exit code."""
    completed = subprocess.run(command, shell=True, capture_output=True, text=True)
    output_text = (completed.stdout or "") + (completed.stderr or "")

    content = (
        f"Command:\n{command}\n\n"
        f"Output:\n{output_text.strip() or '<no output>'}\n\n"
        f"Exit Code: {completed.returncode}\n"
    )

    with open(os.path.join("evidence", filename), "w", encoding="utf-8") as evidence_file:
        evidence_file.write(content)


def main() -> None:
    """Generate all rubric evidence output files."""
    python_exe = "c:/Users/Adneya Khatate/Documents/Coursera/.venv/Scripts/python.exe"

    run_and_save(
        "2b_import_test_output.txt",
        f'"{python_exe}" -c "from EmotionDetection.emotion_detection import emotion_detector; print(emotion_detector(\'I am glad this happened\'))"',
    )
    run_and_save(
        "3b_output_format_test.txt",
        f'"{python_exe}" -c "from EmotionDetection.emotion_detection import emotion_detector; print(emotion_detector(\'I am really mad about this\'))"',
    )
    run_and_save(
        "4b_package_validation_output.txt",
        f'"{python_exe}" -c "import EmotionDetection; print(callable(EmotionDetection.emotion_detector)); print(EmotionDetection.__all__)"',
    )
    run_and_save("5b_unit_test_output.txt", f'"{python_exe}" -m unittest -v')
    run_and_save("8b_pylint_output.txt", f'"{python_exe}" -m pylint server.py')

    print("evidence_generated")


if __name__ == "__main__":
    main()
