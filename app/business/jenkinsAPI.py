#导入依赖
import jenkins
import time
#定义远程的jenkins master server 的url以及Port
jenkins_server_url = 'http://10.2.1.92:8080/jenkins/'
#定义用户的userid 和 apitoken(在jenkins中生成)
user_id = 'admin'
api_token = '11d8c79994b1e6d554c857b1d96fcf4dfe' #测试服务器

#实例化jenkins对象，连接远程的jenkins master server
server = jenkins.Jenkins(jenkins_server_url,username=user_id,password=api_token)
jobName1='pubTest1'
jobName2='pubTest2'

def buildJob():
    '''
    触发自动化测试 automationTest,ScriptTest
    :return: 构建状态
    '''
    buildResult={}

    try:
        next_bn = server.get_job_info(jobName2)['nextBuildNumber']
    except:
        buildResult['msg']='next_bn获取异常，重试'
        print('next_bn获取异常，重试')
        time.sleep(5)
        next_bn = server.get_job_info(jobName2)['nextBuildNumber']
    else:
        buildResult['next_bn']=next_bn
        print('本次执行的jenkins job编号为：', next_bn)

    try:
        server.build_job(jobName2)
    except:
        buildResult['msg'] = '启动jenkinsjob异常，重试'
        print("启动jenkinsjob异常，重试")
        time.sleep(5)
        server.build_job(jobName2)
    else:
        buildResult['msg'] = 'jenkins job启动成功'

    # 启动一个job的时候经常会有延迟的，这是个经验值，暂定10秒，可根据实际情况进行更改。
    time.sleep(10)
    sleeptime = 0
    while sleeptime < 50:

        try:
            server.get_build_info(jobName2, next_bn)['building']
        except:
            time.sleep(5)
            buildResult['msg'] = 'jenkins job还没有启动起来，继续等待5秒...'
            print("jenkins job还没有启动起来，继续等待5秒...")
            sleeptime = sleeptime + 5
        else:
            buildResult['msg'] = 'jenkins job启动成功'
            print("jenkins job启动成功")
            sleeptime = 50
    print("sleeptime", sleeptime)
    print("退出sleep循环")
    return buildResult


if __name__ == '__main__':
    b=buildJob()
    print(b)