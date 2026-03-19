

# ensureNeverFrozen

Error since 2.1

```kotlin
fun Any.ensureNeverFrozen()(source)
```

```kotlin
import kotlin.native.concurrent.*

fun main() {
    // Any object can be protected from freezing
    val counter = Counter()
    counter.ensureNeverFrozen()

    // Trying to freeze it will throw an exception
    try {
        counter.freeze()
    } catch (e: IllegalStateException) {
        println("Cannot freeze: ${e.message}")
    }
}

class Counter {
    var value = 0
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.native.concurrent/ensure-never-frozen.html)

    