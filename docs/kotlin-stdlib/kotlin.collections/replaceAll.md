

# replaceAll

Replaces each element in the list with a result of a transformation specified.

```kotlin
@ExperimentalNativeApiactual fun <T> MutableList<T>.replaceAll(transformation: (T) -> T)(source)
```

```kotlin
import kotlin.experimental.ExperimentalNativeApi

fun main() {
    val numbers = mutableListOf(1, 2, 3, 4)
    numbers.replaceAll { it * 2 }
    println(numbers)   // Output: [2, 4, 6, 8]
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/replace-all.html)

    