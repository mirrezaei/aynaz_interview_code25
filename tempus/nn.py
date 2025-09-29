import sys
import tensorflow as tf
import random
import numpy as np

#LR:0.001
#[0.8679245283018868, 0.8490566037735849, 0.9056603773584906, 0.8490566037735849, 0.8490566037735849, 0.7924528301886793, 0.9056603773584906, 0.8301886792452831, 0.7735849056603774, 0.9056603773584906]
#Average on 10 experiments: 0.8528301886792453
#Std on 10 experiments: 0.04368240340675556

#LR:0.0001
#[0.8867924528301887, 0.7924528301886793, 0.9433962264150944, 0.8490566037735849, 0.9056603773584906, 0.8301886792452831, 0.8301886792452831, 0.9245283018867925, 0.8867924528301887, 0.7735849056603774]
#Average on 10 experiments: 0.8622641509433961
#Std on 10 experiments: 0.05339989320032039

def trainTest(x,y):
    train_x=[]
    test_x=[]
    train_y=[]
    test_y=[]
    ratio=10
    combined = list(zip(x, y))
    random.shuffle(combined)
    x[:], y[:] = zip(*combined)
    testLen=int(len(x)/ratio)
    for i in range(testLen):
        test_x.append(x[i])
        if (y[i] == 1):
            test_y.append([0, 1])
        else:
            test_y.append([1, 0])
    for i in range(testLen,len(x)):

        train_x.append(x[i])
        if (y[i] == 1):
            train_y.append([0, 1])
        else:
            train_y.append([1, 0])
    return train_x,test_x,train_y,test_y




def createBatch(data,y,batch_size):
    batchInd=0
    batches=[]
    y_batches=[]
    new_batch = []
    new_y_batches=[]
    combined = list(zip(data, y))
    random.shuffle(combined)
    data[:], y[:] = zip(*combined)
    for i in range(len(data)):
        if(batchInd<batch_size):
            new_batch.append(data[i])
            new_y_batches.append(y[i])
            batchInd=batchInd+1
        else:
            batches.append(new_batch)
            y_batches.append(new_y_batches)
            new_batch=[]
            new_y_batches=[]
            batchInd=0
    return batches,y_batches

def initialize_model(sess) -> None:
    init_op = tf.group(tf.global_variables_initializer(),
                           tf.local_variables_initializer())
    sess.run(init_op)


def get__data_tarin_X_label_y(dir_path):
    train_X = []
    y =[]
    i = 0;
    try:
        for line in open(dir_path):
            if len(line.strip())>1 and line.strip() != '\n' and i >0:
                data_tokens = line.split("\t")
                # Convert all strings in a list to int
                data_tokens = list(map(int, data_tokens))
                train_X.append(data_tokens[1:])
                y.append(data_tokens[0])
            i+=1
    except:
        print ("*********************" + + str(sys.exc_info()[0]))
    return train_X, y

def classifier(x,y):
    train_x, test_x, train_y, test_y = trainTest(x, y)
    sess = tf.Session()
    input=tf.placeholder(tf.float32,[None,16562],name='input_data')
    gold=tf.placeholder(tf.int64,[None,2],name="True_labels")
    l1=tf.layers.dense(input,2,trainable=True,activation=tf.nn.sigmoid)
    loss=tf.nn.softmax_cross_entropy_with_logits(labels=gold,logits=l1)
    loss=tf.reduce_mean(loss)
    optimizer = tf.train.AdamOptimizer(learning_rate=0.0001)
    train_step = optimizer.minimize(loss)
    initialize_model(sess)
    for epoch in range(40):
        epoch_loss=0
        batches, y_batches = createBatch(train_x, train_y, 10)
        for step, batch_data in enumerate(batches):
            fetch_list = [loss,train_step,l1]
            result = sess.run(fetch_list, feed_dict={input:batch_data,gold:y_batches[step]})
            batch_loss = result[0]
            epoch_loss=epoch_loss+batch_loss
            print("Epoch:"+str(epoch)+", Batch:"+str(step)+", loss: " +str(batch_loss))
        print("***************Epoch "+str(epoch)+", loss:"+str(epoch_loss/len(batches)))

    result = sess.run(l1, feed_dict={input:test_x,gold:test_y})
    acc=0
    for ind,sample in enumerate(result):
        pred=np.argmax(sample)
        if(np.argmax(test_y[ind])==pred):
            acc=acc+1
    print("Total acc:" +str(acc/len(test_y)))
    return acc/len(test_y)

x, y = get__data_tarin_X_label_y('binary_classification.txt')
nuExp=10
accClassifier=[]
for i in range(nuExp):
    accClassifier.append(classifier(x,y))
print(accClassifier)
print("Average on "+str(nuExp)+" experiments: "+str(np.mean(accClassifier)))
print("Std on "+str(nuExp)+" experiments: "+str(np.std(accClassifier)))
