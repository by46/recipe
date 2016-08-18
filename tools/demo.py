from jenkins import Jenkins

if __name__ == '__main__':
    jenkins = 'http://scdfis01:8080', 'benjamin', '123456'
    client = Jenkins(*jenkins)
    client.delete_job('demo')
    with open('config.xml', 'rb') as f:
        client.create_job('demo', f.read())
