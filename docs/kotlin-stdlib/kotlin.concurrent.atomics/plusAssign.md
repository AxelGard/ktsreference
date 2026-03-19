

# plusAssign

Atomically adds the given value to the current value of this AtomicInt.

```kotlin
@ExperimentalAtomicApioperator fun AtomicInt.plusAssign(delta: Int)(source)
```

```kotlin
import kotlin.concurrent.atomics.*

@OptIn(ExperimentalAtomicApi::class)
fun main() {
    val counter = AtomicInt(0)

    // Atomically add 3
    counter += 3

    // Atomically add 7
    counter += 7

    println("Counter value: ${counter.value}")   // prints 10
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.concurrent.atomics/plus-assign.html)

    