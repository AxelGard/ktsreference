

# isFrozen

Error since 2.1

```kotlin
val Any?.isFrozen: Boolean(source)
```

```kotlin
import kotlin.native.concurrent.*

fun main() {
    val numbers = mutableListOf(1, 2, 3)
    println("Before freezing: ${numbers.isFrozen}")   // false

    numbers.freeze()

    println("After freezing: ${numbers.isFrozen}")    // true
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.native.concurrent/is-frozen.html)

    