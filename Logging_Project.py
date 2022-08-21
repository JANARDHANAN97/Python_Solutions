#!/usr/bin/env python
# coding: utf-8

# In[1]:


import logging
import requests
import os


# In[54]:


logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(process)d - %(name)s - %(levelname)s - %(message)s")


# In[81]:



def test_decorator(func):    
    # implement with code that does the following
    #
    # 1. implement this as a decorator ( see PEP 318 – Decorators for Functions and Methods: https://peps.python.org/pep-0318/ ).  This decorator decorates the function 'test_rest_api' below
    # 2. The decorator
    # 2.1    logs all arguments that are passed to the decorated function using the logging API ( see https://docs.python.org/3/howto/logging.html#logging-basic-tutorial and https://docs.python.org/3/library/logging.html)
    #             example of obtaining a logger:  logger = logging.getLogger("mylogger")
    # 2.2    sets the environment variable TRACKING_URI (set it to any URL string that you like) before calling the decorated function.  
    # 2.3    injects values for the keyword argument 'logger' to the decorated function.  See above for sample code to get a 'logger'
    # 2.4    And unsets this environment variable after the call to the decorated function completes    
    # 2.5    catches any exceptions raised by the decorated function and logs the exception
    #pass
    def logging_func(*args, **kwargs): 
        logger = logging.getLogger("Logging_test")
        os.environ["TRACKING_URI"] = "new_var"
        logger.info("Keyword auruments:{}".format(*args))
        logger.info("Non Keyword auruments: {}".format(kwargs))
        logger.info("API Arguments: url={}, headers={}, params={}, json={})".format(args[0], args[1], args[2], args[3]))
        func(*args, logger = logger,  **kwargs)
        os.environ.pop('TRACKING_URI', None)
    return logging_func


# In[83]:


@test_decorator
def test_rest_api(url, headers, params, body, *args, logger=None, **kwargs):
    """
    this function makes a POST call to the specified 'url' using 'headers', 'params' (query params) and 'body' (POST data)
    
    this function is decorated with the decorator 'test_decorator' (see above)
    
    implement code that
    1. POSTs to the specified rest API using the arguments 'url', 'headers', 'params' and 'body': POST <url>
    2. uses the 'logger' argument to log the response of the REST API ( see https://docs.python.org/3/howto/logging.html#logging-basic-tutorial and https://docs.python.org/3/library/logging.html)
    3. uses the 'logger' argument to log the environment variable 'TRACKING_URI'


    Args:
        url (str): REST API URL that supports a POST
        headers: headers to be passed to the the POST request
        params: query arguments / parameters to be passed to the POST request
        body: the data (body) for the POST request
        logger : a logger object.  You can obtain a logger using logging.getLogger(<some_name_for_logger>).  See https://docs.python.org/3/howto/logging.html#logging-basic-tutorial for details
    """
    #env_var = os.environ["env1"]
    resp = requests.post(url=url, headers=headers, params=params, json=body)
    logger.info("Response {}".format(resp))
    logger.info("Response Text {}".format(resp.text))
    logger.info("!!! Done")

# Echo API | Postman Learning Center: https://learning.postman.com/docs/developer/echo-api/
test_rest_api('https://postman-echo.com/post', {'Authorization':'Basic abcdefgh'}, {'key1':'value1', 'key2':'value2'}, {'postkey1':'postval1', 'postkey2':'postval2'}) 
#print(resp.text)


# In[ ]:




