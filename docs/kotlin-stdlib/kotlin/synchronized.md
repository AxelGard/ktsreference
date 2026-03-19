

# synchronized

Warning since 1.6

```kotlin
inline fun <R> synchronized(lock: Any, block: () -> R): R(source)
```

```kotlin
import kotlin.concurrent.thread

var counter = 0
val lock = Any()

fun increment() {
    synchronized(lock) {
        counter++
    }
}

fun main() {
    val threads = List(10) {
        thread {
            repeat(1000) { increment() }
        }
    }
    threads.forEach { it.join() }
    println("Counter: $counter")   // Should print 10000
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/synchronized.html)

    