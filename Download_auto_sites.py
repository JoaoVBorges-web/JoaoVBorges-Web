#!/usr/bin/env python
# coding: utf-8

# In[10]:


from selenium import webdriver

navegador = webdriver.Chrome()

navegador.get("https://ri.magazineluiza.com.br/show.aspx?idCanal=CHN0/Z4bUSgrS8IkQeL+Wg==")
navegador.find_element_by_xpath('//*[@id="52UstABBxF8k7Q9IXxA3iw=="]').click()


# In[ ]:





# In[ ]:




