

# update

Atomically updates the value of this AtomicInt with the value obtained by calling the transform function on the current value.

```kotlin
@ExperimentalAtomicApiexpect inline fun AtomicInt.update(transform: (Int) -> Int)(source)
```

```kotlin
import kotlin.concurrent.atomic

fun main() {
    val counter = atomic(0)

    // Atomically add 1 to the current value
    val newValue = counter.update { it + 1 }

    println("Initial value: 0")
    println("Updated value: $newValue")   // prints 1
    println("Current value via counter.value: ${counter.value}") // prints 1
}
```


[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.concurrent.atomics/update.html)

    