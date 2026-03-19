

# asKotlinAtomic

Casts the given java.util.concurrent.atomic.AtomicInteger instance to AtomicInt.

```kotlin
@ExperimentalAtomicApifun AtomicInteger.asKotlinAtomic(): AtomicInt(source)
```

```kotlin
import java.util.concurrent.atomic.AtomicInteger
import kotlin.concurrent.atomics.*

@OptIn(ExperimentalAtomicApi::class)
fun main() {
    // Create a Java AtomicInteger
    val javaAtomic = AtomicInteger(0)

    // Cast it to Kotlin's AtomicInt
    val atomicInt = javaAtomic.asKotlinAtomic()

    // Use Kotlin AtomicInt APIs
    atomicInt.increment()      // atomically increments the value
    atomicInt.add(5)           // atomically adds 5
    val current = atomicInt.get()

    println("Current value: $current")  // prints: Current value: 6
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.concurrent.atomics/as-kotlin-atomic.html)

    