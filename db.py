from typing import List, Any, Optional
import sqlite3


class DB:

    # db 연결
    def init_db(self) -> Any:
        pass

    # 초기 db 테이블 생성
    def create_table(self) -> Any:
        pass

    # db 데이터 리스트 반환
    def list(self, dns: str) -> Any:
        pass

    # db에 dns 추가
    def add_data_to_file(self, dns: str) -> Any:
        pass

    # 사용자가 입력한 dns 중 이미 존재하는 dns 있는지 확인
    def is_exists(self, dns: str) -> bool:
        pass

    # db에 있는 dns 데이터 삭제하기
    def delete_data(self, dns: str) -> Any:
        pass
