#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


# 수강기록 관련하여 분석하기(어느 시점에 수강생이 떠나는가)
# 수강기록 데이터 가져오기
enroll = pd.read_csv("./enrolleds_detail.csv")
enroll


# In[3]:


# 강의별로 강의 완료 학생 수 구하기
enroll_detail = enroll.groupby('lecture_id')['user_id'].count()
enroll_detail


# In[4]:


import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'Malgun Gothic'

plt.figure(figsize=(22,5))
plt.bar(enroll_detail.index, enroll_detail)
plt.title('강의에 따른 수강완료 수의 합계')
plt.xticks(rotation = 90)
plt.show()


# In[5]:


# 강의정보 데이터 가져오기
lectures = pd.read_csv('./lectures.csv')
lectures


# In[7]:


# 데이터 프레임 만들기
lecture_count = pd.DataFrame(enroll_detail)
lecture_count


# In[8]:


# index 재설정
lecture_count = lecture_count.reset_index()
lecture_count


# In[9]:


# 칼럼이름 바꾸기
lecture_count = lecture_count.rename(columns={'user_id':'count'})
lecture_count


# In[10]:


# index 재설정
lectures = lectures.set_index('lecture_id')
lectures


# In[12]:


# 데이터 합치기
full_lecture = lecture_count.join(lectures, on='lecture_id')
full_lecture


# In[13]:


plt.figure(figsize=(22,5))
plt.bar(full_lecture['title'], full_lecture['count'])
plt.title('강의에 따른 수강완료 수의 합계')
plt.xlabel('강의명')
plt.xticks(rotation=90)
plt.show()


# In[ ]:




