import re

from src.adapters.repositories.word_repository import WordRepository
from src.usecases.pronunciation.get_pronunciation_usecase import GetPronunciationUseCase
from src.usecases.pronunciation.requests.get_pronunciation_request import GetPronunciationRequest
from src.usecases.pronunciation.responses.get_pronunciation_response import GetPronunciationResponse


class GetPronunciationInteractor(GetPronunciationUseCase):
    def __init__(self, word_repo: WordRepository):
        self._word_repo = word_repo

    def handle(self, request: GetPronunciationRequest) -> GetPronunciationResponse:
        splited_words = [re.sub("['\",.?+:;*!#$%&]", "", word.lower()) for word in request.words.split()]

        words = self._word_repo.find_by_names(splited_words)
        phonetic_map = {word.name: word.phonetic_symbol for word in words if word}

        pronunciation = [phonetic_map[sw] if phonetic_map.get(sw) else "*" for sw in splited_words]

        return GetPronunciationResponse(pronunciation)
