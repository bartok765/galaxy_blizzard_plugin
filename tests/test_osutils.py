from osutils import get_directory_size


def test_get_directory_size(tmp_path):
    def create_file(path: str, content: bytes) -> int:
        path.parent.mkdir(exist_ok=True, parents=True)
        return path.write_bytes(content)

    expected_size = sum(
        create_file(p, c) for p, c in [
            (tmp_path / 'readme.txt', b'Readme content'),
            (tmp_path / 'assets' / 'de.pack', b'dummy binary file content'),
            (tmp_path / 'bin' / 'game.exe', b'0\05sdcdsdj9asfsdf\nfaf22e' * 1000000)
        ]
    )
    assert get_directory_size(tmp_path) == expected_size
