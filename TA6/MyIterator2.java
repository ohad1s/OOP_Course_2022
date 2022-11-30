package TA6;
import java.util.Iterator;

public class MyIterator2 <Type> implements Iterable<Type> {



        private Type[] arrayList;
        private int currentSize;

        public MyIterator2(Type[] newArray) {
            this.arrayList = newArray;
            this.currentSize = arrayList.length;
        }

        @Override
        public Iterator<Type> iterator() {
            Iterator<Type> it = new Iterator<Type>() {

                private int currentIndex = 0;

                @Override
                public boolean hasNext() {
                    return currentIndex < currentSize && arrayList[currentIndex] != null;
                }

                @Override
                public Type next() {
                    return arrayList[currentIndex++];
                }

                @Override
                public void remove() {
                    throw new UnsupportedOperationException();
                }
            };
            return it;
        }
    }

