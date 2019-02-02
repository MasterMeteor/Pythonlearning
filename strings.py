#coding=utf-8
'''
String:是由字母，下划线，数字组成的一串字符
单引号双引号都行
从左往右，从0开始，最大范围是字符串长度少1
从右往左，从-1开始，最大范围长度是字符串开头
若要获取字符串，变量[头下标:尾下标]
下标从0开始算起，可以是正，负
下标可以为空
'''


#------------------
dss='hello xin'
print('dss',dss)

#1
print('\n#1')
s2=dss[1:];print('s2,',s2)
s3=dss[1:3];print('s3,',s3)
s4=dss[:3];print('s4,',s4)

#2
print('\n#2')
s2=dss[-1];print('s2,',s2)
s3=dss[1:-2];print('s3,',s3)
dn=len(dss);print('dn,',dn)

#3
print('\n#3')
print('s2+s3,',s2+s3)
print('s3*2,',s3*2)


