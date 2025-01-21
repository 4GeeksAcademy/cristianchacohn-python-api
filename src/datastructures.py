"""
Update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint


class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name        
        self._members = [{'id': 10, 'last_name': self.last_name, 'name': 'John', 'age': 33, 'lucky_number': [7, 13, 22]},
                         {'id': self._generate_id(), 'last_name': self.last_name, 'name': 'Jane', 'age': 35, 'lucky_number': [10, 14, 3]},
                         {'id': self._generate_id(), 'last_name': self.last_name, 'name': 'Jimmy', 'age': 5, 'lucky_number': [1]}]
        
    # Read-only: Use this method to generate random members ID's when adding members into the list
    def _generate_id(self):
        return randint(0, 99999999)

    def add_member(self, member):
        member['id'] = self._generate_id()
        member['lastname'] = self.last_name
        self._members.append(member)
        return

    def delete_member(self, id):
        members = [row for row in self._members if row['id'] != id] 
        self._members = members
        return

    def get_member(self, id):
        member = [row for row in self._members if row['id'] == id] 
        return member
    
    def get_all_members(self):
        return self._members
