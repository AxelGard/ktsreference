

# updateAndFetch

Atomically updates the value of this AtomicInt with the value obtained by calling the transform function on the current value and returns the new value.

```kotlin
@ExperimentalAtomicApiexpect inline fun AtomicInt.updateAndFetch(transform: (Int) -> Int): Int(source)
```

```kotlin
import kotlin.concurrent.atomics.AtomicInt
import kotlin.concurrent.atomics.ExperimentalAtomicApi

@OptIn(ExperimentalAtomicApi::class)
fun main() {
    val counter = AtomicInt(5)

    // Atomically double the current value and obtain the new value
    val newValue = counter.updateAndFetch { it * 2 }

    println("New value: $newValue")   // Prints: New value: 10
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.concurrent.atomics/update-and-fetch.html)

    