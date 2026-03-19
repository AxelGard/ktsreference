

# minusAssign

Atomically subtracts the given value from the current value of this AtomicInt.

```kotlin
@ExperimentalAtomicApioperator fun AtomicInt.minusAssign(delta: Int)(source)
```

```kotlin
import kotlin.concurrent.atomic
import kotlin.concurrent.ExperimentalAtomicApi

@OptIn(ExperimentalAtomicApi::class)
fun main() {
    val counter = atomic(10)     // AtomicInt with initial value 10
    counter -= 3                // atomically subtract 3
    println(counter.value)      // prints 7
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.concurrent.atomics/minus-assign.html)

    