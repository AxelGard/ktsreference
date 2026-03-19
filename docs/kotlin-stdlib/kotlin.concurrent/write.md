

# write

Executes the given action under the write lock of this lock.

```kotlin
@IgnorableReturnValueinline fun <T> ReentrantReadWriteLock.write(action: () -> T): T(source)
```

```kotlin
import java.util.concurrent.locks.ReentrantReadWriteLock

val lock = ReentrantReadWriteLock()
val sharedData = mutableMapOf<String, Int>()

fun updateCount(key: String, value: Int) {
    lock.write {
        sharedData[key] = value
    }
}

fun readCount(key: String): Int? {
    return lock.read {
        sharedData[key]
    }
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.concurrent/write.html)

    