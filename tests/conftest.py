import pytest
 
@pytest.fixture
def user_data():
 return{
 "username":"testuser",
 "password":"test123"
 }
# import os
# import pytest
# @pytest.fixture(scope="session",autouse=True)
# def create_resukts_folder():
# os.makedirs("test-results",exist_ok=True)