import os
from typing import Any, Optional


class SystemAccess:
    # 입력된 dns 리스트 반환
    def list(self) -> Any:
        pass

    # 존재 하는 dns 인지 확인
    def is_exists(self, dns: str) -> bool:
        pass

    # dns 삭제
    def delete(self, dns: str) -> Any:
        pass

    # dns 추가
    def append(self, dns: str) -> Any:
        pass
