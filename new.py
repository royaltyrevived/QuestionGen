from rake_nltk import Rake
R= Rake()
text_to_extract_keywords= input('Enter the Question you want to enter:')
R.extract_keywords_from_text(text_to_extract_keywords)
print(R.get_ranked_phrases_with_scores())
with open("temp.txt","w+") as temp_file:
        for line in R.get_ranked_phrases_with_scores():
            temp_file.write("".join(str(line))+"\n")
temp_file.close()
