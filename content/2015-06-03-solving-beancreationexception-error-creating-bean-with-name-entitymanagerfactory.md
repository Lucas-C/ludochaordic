Title: Solving BeanCreationException: Error creating bean with name 'entityManagerFactory'
Date: 2015-06-03 12:06
Tags: lang:en, springboot, bean, maven, version, exception, hibernate
Slug: en-solving-beancreationexception-error-creating-bean-with-name-entitymanagerfactory
---
I've lost quite some time on this error recently :

```
Caused by: org.springframework.beans.factory.BeanCreationException: Error creating bean with name 'entityManagerFactory' defined in class path resource [org/springframework/boot/autoconfigure/orm/jpa/HibernateJpaAutoConfiguration.class]: Invocation of init method failed; nested exception is java.lang.AbstractMethodError: org.hibernate.jpa.boot.internal.EntityManagerFactoryBuilderImpl$4.getConfigurationValues()Ljava/util/Map;
        at org.springframework.beans.factory.support.AbstractAutowireCapableBeanFactory.initializeBean(AbstractAutowireCapableBeanFactory.java:1574)
        at org.springframework.beans.factory.support.AbstractAutowireCapableBeanFactory.doCreateBean(AbstractAutowireCapableBeanFactory.java:539)
        at org.springframework.beans.factory.support.AbstractAutowireCapableBeanFactory.createBean(AbstractAutowireCapableBeanFactory.java:476)
        at org.springframework.beans.factory.support.AbstractBeanFactory$1.getObject(AbstractBeanFactory.java:303)
        at org.springframework.beans.factory.support.DefaultSingletonBeanRegistry.getSingleton(DefaultSingletonBeanRegistry.java:230)
        at org.springframework.beans.factory.support.AbstractBeanFactory.doGetBean(AbstractBeanFactory.java:299)
        at org.springframework.beans.factory.support.AbstractBeanFactory.getBean(AbstractBeanFactory.java:194)
        at org.springframework.context.support.AbstractApplicationContext.getBean(AbstractApplicationContext.java:956)
        at org.springframework.context.support.AbstractApplicationContext.finishBeanFactoryInitialization(AbstractApplicationContext.java:747)
        at org.springframework.context.support.AbstractApplicationContext.refresh(AbstractApplicationContext.java:480)
        at org.springframework.boot.SpringApplication.refresh(SpringApplication.java:686)
        at org.springframework.boot.SpringApplication.run(SpringApplication.java:320)
```

Bottom line: it was due to a mismatch between Spring Boot Hibernate version, and the one I used in my project, defined in `pom.xml`.

Simply make sure that they match, e.g by [looking here for version 1.2.3.RELEASE](https://github.com/spring-projects/spring-boot/blob/24a791898c44087943fe8662354f0de1c41cc108/spring-boot-dependencies/pom.xml#L72).

**EDIT 14/04/2016:** adding a couple of comments that an anonymous visitor tried to post:
> I faced the same exception when including hibernate-search ontop of spring-boot + hibernate + spring-mvc project! What is the exact resolution?

> Resolution: use 4.5.x hibernate-search-orm artifact. works fine with the latest spring-boot. atleast the unit tests are starting to run! :-)
