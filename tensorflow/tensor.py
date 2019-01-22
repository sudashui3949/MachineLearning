#learn tensor

import tensorflow as tf

a = tf.constant([1.0,2.0],name = "a")
b = tf.constant([2.0,3.0],name = "b")

result = tf.add(a,b,name = "add")
print result

result2 = tf.add(result,a,name = "add")
print result2

#sess = tf.Session()
#print sess.run(result2)

sess = tf.Session()
with sess.as_default():
	print "result2 is" ,result2.eval()
	print "result is " ,result.eval()
