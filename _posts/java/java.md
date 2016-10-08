---
title: java学习
---
# java学习

+ gradle 依赖管理工具

gradle 集合了 maven 和 ant 的优点

+ gradle 安装
`gradle -v ` 探测是否安装 如果没有安装

sudo dnf install gradle

[gradle教程](http://www.zircon.me/06-25-2015/about-gradle.html)

项目 目录下会有 
build.gradle
settings.gradle


国内meven 软件源

吐槽：oschina的软件源 很不稳定 不可以使用，还不如国外的

国内最好的是 maven
地址：
http://maven.aliyun.com/nexus/content/groups/public

国内最好用的maven源 阿里云的maven源

创建～/.gradle/init.gradle 文件指定软件源
allprojects{
    repositories {
        def REPOSITORY_URL = 'http://maven.aliyun.com/nexus/content/groups/public'
        all { ArtifactRepository repo ->
            if(repo instanceof MavenArtifactRepository){
                def url = repo.url.toString()
                if (url.startsWith('https://repo1.maven.org/maven2') || url.startsWith('https://jcenter.bintray.com/')) {
                    project.logger.lifecycle "Repository ${repo.url} replaced by $REPOSITORY_URL."
                    remove repo
                }
            }
        }
        maven {
            url REPOSITORY_URL
        }
    }
}
