import re

from src.adapters.repositories.word_repository import WordRepository
from src.request_objects.pronunciation.get_pronunciation_request import GetPronunciationRequest
from src.response_objects.pronunciation.get_pronunciation_response import GetPronunciationResponse
from src.use_cases.pronunciation.get_pronunciation_use_case import AbstractGetPronunciationUseCase


class GetPronunciationUseCase(AbstractGetPronunciationUseCase):
    def __init__(self, word_repo: WordRepository):
        self._word_repo = word_repo

    def handle(self, request: GetPronunciationRequest) -> GetPronunciationResponse:
        splited_words = [re.sub("['\",.?+:;*!#$%&]", "", word.lower()) for word in request.words.split()]

        words = self._word_repo.find_by_names(splited_words)
        phonetic_map = {word.name: word.phonetic_symbol for word in words if word}

        pronunciation = [phonetic_map[sw] if phonetic_map.get(sw) else "*" for sw in splited_words]

        return GetPronunciationResponse(pronunciation)
