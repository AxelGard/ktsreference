

# freeze

Error since 2.1

```kotlin
fun <T> T.freeze(): T(source)
```

```kotlin
import kotlin.native.concurrent.*

fun main() {
    val numbers = mutableListOf(5, 10, 15)
    val frozenNumbers = numbers.freeze()

    thread(start = true) {
        println("Thread sees frozen list: $frozenNumbers")
    }
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.native.concurrent/freeze.html)

    