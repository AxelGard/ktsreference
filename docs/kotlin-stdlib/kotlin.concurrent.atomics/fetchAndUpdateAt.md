

# fetchAndUpdateAt

Atomically updates the element of this AtomicIntArray at the given index using the transform function and returns the old value of the element.

```kotlin
@ExperimentalAtomicApiexpect inline fun AtomicIntArray.fetchAndUpdateAt(index: Int, transform: (Int) -> Int): Int(source)
```

```kotlin
import kotlin.concurrent.atoms.AtomicIntArray
import kotlin.experimental.ExperimentalAtomicApi

@OptIn(ExperimentalAtomicApi::class)
fun main() {
    val array = AtomicIntArray(3)
    array[1] = 42

    val oldValue = array.fetchAndUpdateAt(1) { it + 8 }

    println("Old value: $oldValue")          // 42
    println("New value: ${array[1]}")        // 50
}
```


[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.concurrent.atomics/fetch-and-update-at.html)

    