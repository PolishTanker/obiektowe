class NameValidator:
    def is_valid(self, name: str) -> bool:
        if len(name) <= 2:
            return False
        # New validation: valid names contain only letters (both upper and lower case)
        return bool(name) and all(char.isalpha() for char in name)



class Constituency:

    def __init__(self, parties: list[str]):
        self.__voted: dict[str, bool] = {}
        self.__parties = parties
        self.__n_parties = len(parties)
        self.__votes = [0] * self.__n_parties

        # Check for duplicate parties
        if len(set(parties)) != len(parties):
            raise ValueError("Duplicate party names are not allowed")

    def register_voter(self, voter_name: str):
        if voter_name in self.__voted:
            raise RuntimeError('This person is already registered')
        if not NameValidator().is_valid(voter_name):
            raise RuntimeError('Not a valid name')
        self.__voted[voter_name] = False  # not voted

    def is_registered(self, voter_name: str) -> bool:
        return voter_name in self.__voted

    def can_vote(self, voter_name: str) -> bool:
        return voter_name in self.__voted and not self.__voted[voter_name]

    def vote(self, voter_name: str, party: str):
        if voter_name not in self.__voted:
            raise RuntimeError('Person cannot vote')
        if self.__voted[voter_name]:
            raise RuntimeError('Person already voted')
        if party not in self.__parties:
            raise RuntimeError('No such party')
        idx = self.__parties.index(party)
        self.__votes[idx] += 1
        self.__voted[voter_name] = True  # mark as voted

    def get_votes_of_party(self, party_name: str) -> int:
        if party_name in self.__parties:
            idx = self.__parties.index(party_name)
            return self.__votes[idx]
        else:
            raise RuntimeError('No such party')

    def get_results_as_members_of_parliament(self, parliament_places: int) -> list[int]:
        results = [0] * self.__n_parties
        quotients = []

        for i in range(self.__n_parties):
            for j in range(1, parliament_places + 1):
                quotients.append((self.__votes[i] / j, i))

        quotients.sort(reverse=True)

        for i in range(parliament_places):
            _, party_index = quotients[i]
            results[party_index] += 1

        return results


