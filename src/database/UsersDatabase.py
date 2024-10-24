from .GeneralDatabase import GeneralMethods 



class UserMethods(GeneralMethods):
      
    async def fetch_all_users():
        allUsers = await GeneralMethods.execute_query_async("SELECT u.* FROM usuario u")  # Await the result
        return allUsers

