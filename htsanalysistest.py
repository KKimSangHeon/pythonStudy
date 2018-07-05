from pprint import pprint
from konlpy.tag import Twitter
import pandas as pd
from konlpy.utils import pprint



twi_tagger = Twitter()
temp_sen = u"마늘치킨 냠냠 쩝쩝쩝 ㅋ"
pprint(twi_tagger.pos(temp_sen, norm=True, stem=True))

korean_review_df = pd.read_csv( "ratings_test.txt", header=0, delimiter="\t", quoting=3, encoding="utf-8" )
# 제대로 읽혔는지 확인
len(korean_review_df) # 50000개의 리뷰데이터
# 읽은 리뷰데이터셋 확인
korean_review_df[:5]

words_temp = twi_tagger.pos(korean_review_df["documnet"][3], norm = True, stem = True)
pprint(words_temp)
