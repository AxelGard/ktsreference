

# read

Executes the given action under the read lock of this lock.

```kotlin
@IgnorableReturnValueinline fun <T> ReentrantReadWriteLock.read(action: () -> T): T(source)
```

```kotlin
import java.util.concurrent.locks.ReentrantReadWriteLock
import kotlin.concurrent.read

val lock = ReentrantReadWriteLock()
val sharedState = mutableMapOf<String, Int>()

fun readValue(key: String): Int? = lock.read {
    sharedState[key]
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.concurrent/read.html)

    