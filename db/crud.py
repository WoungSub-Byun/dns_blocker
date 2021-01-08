from typing import Any


class DBController:
    # db 연결
    def __init__(self) -> Any:
        pass

    # db 저장된 dns 반환
    def list(self, dns: str) -> Any:
        pass

    # db에 dns 추가
    def create(self, dns: str) -> Any:
        pass

    # 사용자가 입력한 dns 중 이미 존재하는 dns 있는지 확인
    def is_exist(self, dns: str) -> bool:
        pass

    # db에 있는 dns 데이터 삭제하기
    def delete(self, dns: str) -> Any:
        pass
