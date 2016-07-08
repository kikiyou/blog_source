
### sqlalchemy的使用

+ 连接数据库


    from sqlalchemy import create_engine
    engine = create_engine('sqlite:///:memory:', echo=True)

echo=True  调试的时候使用，显示sql代码

sqlite:///DB_PATH

+ 简介及


    from sqlalchemy.ext.declarative import declarative_base
    Base = declarative_base()

+ 定义继承


    from sqlalchemy import Column, Integer, String
    class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    password = Column(String)
    def __repr__(self):
        return "<User(name='%s', fullname='%s', password='%s')>" % (
                             self.name, self.fullname, self.password)


+ 创建表


    Base.metadata.create_all(engine)

+ 对映射的类创建实例


    ed_user = User(name='ed', fullname='Ed Jones', password='edspassword')
    ed_user.name
    str(ed_user.id)

  注：通过上面语句可以修改User表中的数据，但是会发现ed_user.id是空的，因为这时修改的数据，没有进行数据持久化，没有写入数据库中。


+ 创建session 使数据持久化


    from sqlalchemy.orm import sessionmaker
    Session = sessionmaker(bind=engine)
    session = Session()

+ 添加一条记录


    ed_user = User(name='ed', fullname='Ed Jones', password='edspassword')
    session.add(ed_user)
    our_user = session.query(User).filter_by(name='ed').first()

   注:上面的方法是添加一条，并且查询 name = 'ed' 的记录

+ 添加多条

session.add_all([
...     User(name='wendy', fullname='Wendy Williams', password='foobar'),
...     User(name='mary', fullname='Mary Contrary', password='xxg527'),
...     User(name='fred', fullname='Fred Flinstone', password='blah')])

+ 修改ed_user的密码
ed_user.password = 'f8s7ccs'

+ 查看那些被修改但是没有提交的脏数据
session.dirty
IdentitySet([<User(name='ed', fullname='Ed Jones', password='f8s7ccs')>])

+ 查看新添加的数据
session.new  # 查看到有新添加的三条
IdentitySet([<User(name='wendy', fullname='Wendy Williams', password='foobar')>,
<User(name='mary', fullname='Mary Contrary', password='xxg527')>,
<User(name='fred', fullname='Fred Flinstone', password='blah')>])

+ 提交上面更改 写入到磁盘


    session.commit()
    ed_user.id
注：这里就可以看到 id的值了

+ 回滚


    ed_user.name = 'Edwardo'
    fake_user = User(name='fakeuser', fullname='Invalid', password='12345')
    session.add(fake_user)
    session.query(User).filter(User.name.in_(['Edwardo', 'fakeuser'])).all()
注：通过上面的查询，可以直到数据已经写入到当前的事务


    session.rollback()
    ed_user.name
u'ed'


    fake_user in session
False
注： 可以看到fake_user不存在 session中

session.query(User).filter(User.name.in_(['ed', 'fakeuser'])).all()
通过上面查询，无法查到fakeuser用户
