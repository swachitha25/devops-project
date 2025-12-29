from log_analyzer import analyze_log

def test_log_analysis(tmp_path):
    log_file = tmp_path / "sample.log"
    log_file.write_text(
        "INFO Application started\n"
        "WARNING Disk usage high\n"
        "ERROR Failed to connect\n"
        "ERROR Timeout occurred\n"
    )

    result = analyze_log(str(log_file))
    assert result["INFO"] == 1
    assert result["WARNING"] == 1
    assert result["ERROR"] == 2
