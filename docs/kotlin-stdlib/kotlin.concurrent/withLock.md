

# withLock

Executes the given action under this lock.

```kotlin
@IgnorableReturnValueinline fun <T> Lock.withLock(action: () -> T): T(source)
```

```kotlin
import java.util.concurrent.locks.ReentrantLock

val lock = ReentrantLock()
var counter = 0

fun increment() {
    lock.withLock {
        counter++
    }
}

fun getCounter(): Int = lock.withLock { counter }
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.concurrent/with-lock.html)

    