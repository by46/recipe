from jenkins import Jenkins

if __name__ == '__main__':
    jenkins_url = 'http://scdfis01:8080'
    client = Jenkins(jenkins_url, 'recipe', 'recipe')
    client.delete_view('recipe')
