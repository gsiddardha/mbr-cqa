import urllib2
import gzip
import json
import os
from StringIO import StringIO

class Fetcher:
    """ Fetcher class with implementations of getQuestions, getAnswers and getTags"""

    def getQuestions(self, tag, pages):
        """ Gets all questions for a given tag. Fetches the number of pages requested"""
        content = []
        url = "http://api.stackexchange.com/2.0/questions?page=%s&order=desc&sort=creation&tagged="+tag+"&site=stackoverflow"
        # Get the page, save it on disk, append it to content
        for page in range(pages):
            page_id = page+1
            if os.path.isfile('data/'+tag+'_'+str(page_id)+'.txt'):
                print "Tag - "+tag+" Page - " + str(page_id) + " already exists"
                continue
            print "Getting page " + str(page_id)
            temp_content = StringIO(urllib2.urlopen(url % str(page_id)).read())
            final_content = gzip.GzipFile(fileobj=temp_content).read()
            f = open("data/" + tag+"_"+str(page_id)+".txt", "w")
            f.write(final_content)
            f.close()
            content.append(json.loads(final_content))
        return content

    def getAnswers(self, tag):
        """ Gets all answers for a given tag."""
        f = open('data/'+tag+'_final.txt', 'r')
        questions = json.loads(f.read())
        f.close()
        url = "http://api.stackexchange.com/2.0/questions/%s/answers?order=desc&sort=activity&site=stackoverflow"
        batches = [questions[i:i+5] for i in range(0, len(questions), 5)]
        content = []
        # For each batch - get the page, save it on disk, append it to content
        # batch size set to 5 (change batches line if another size is required)
        for (counter, batch) in enumerate(batches):
            if os.path.isfile('data/'+tag+'_answers_'+str(counter+1)+'.txt'):
                print "Tag - "+tag+" Page - "+str(counter+1)+" already exists"
                continue

            ids = str(batch[0]["question_id"])
            for question in batch[1:]:
                ids += ";"+str(question["question_id"])
            print "Getting page " + str(counter+1)
            temp_content = StringIO(urllib2.urlopen(url % ids).read())
            final_content = gzip.GzipFile(fileobj=temp_content).read()
            f = open('data/'+tag+'_answers_'+str(counter)+'.txt', 'w')
            f.write(final_content)
            f.close()
            content.append(json.loads(final_content))
        return content

    def getTags(self, tag):
        """ Gets all users for a given tag."""
        f = open('data/'+tag+'_users.txt', 'r')
        users = json.loads(f.read())
        f.close()
        url = "http://api.stackexchange.com/2.0/users/%s/tags?order=desc&sort=popular&site=stackoverflow"
        batches = [users[i:i+3] for i in range(0, len(users), 3)]
        content = []
        # For each batch - get the page, save it on disk, append it to content
        # batch size set to 3 (change batches line if another size is required)
        for (counter, batch) in enumerate(batches):
            if os.path.isfile('data/'+tag+'_tags_'+str(counter+1)+'.txt'):
                print "Tag - "+tag+" Page - "+str(counter+1)+" already exists"
                continue
            ids = str(batch[0])
            for user in batch[1:]:
                ids += ";"+str(user)
            print "Getting tags " + str(counter+1)
            temp_content = StringIO(urllib2.urlopen(url % ids).read())
            final_content = gzip.GzipFile(fileobj=temp_content).read()
            f = open('data/'+tag+'_tags_'+str(counter+1)+'.txt', 'w')
            f.write(final_content)
            f.close()
            content.append(json.loads(final_content))
        return content
        
    def getUserData(self, tag):
        f = open('data/'+tag+'_users.txt', 'r')
        users = json.loads(f.read())
        f.close()
        url = "https://api.stackexchange.com/2.0/users/%s?order=desc&sort=reputation&site=stackoverflow"
        batches = [users[i:i+10] for i in range(0, len(users), 10)]
        content = []
        # For each batch - get the page, save it on disk, append it to content
        # batch size set to 3 (change batches line if another size is required)
        for (counter, batch) in enumerate(batches):
            if os.path.isfile('data/'+tag+'_user_data_'+str(counter+1)+'.txt'):
                print "Data - "+tag+" Page - "+str(counter+1)+" already exists"
                continue
            ids = str(batch[0])
            for user in batch[1:]:
                ids += ";"+str(user)
            print "Getting Data " + str(counter+1)
            temp_content = StringIO(urllib2.urlopen(url % ids).read())
            final_content = gzip.GzipFile(fileobj=temp_content).read()
            f = open('data/'+tag+'_user_data_'+str(counter+1)+'.txt', 'w')
            f.write(final_content)
            f.close()
            content.append(json.loads(final_content))
        return content


print "Creating the content fetcher ..."
content_fetcher = Fetcher()
print "Starting to fetch content ..."
c_questions = content_fetcher.getQuestions("c", 100)
print "Finished fetching ..."

print "Getting answers ..."
c_answers = content_fetcher.getAnswers("c")
print "Finished fetching ..."

print "Getting tags ..."
c_tags = content_fetcher.getTags("c")
print "Fininshed fetching ..."

# diversity in recommendation
# cooling function
# complexity of question. ranking the question and recommending tough ones to expert and easy ones to novice
