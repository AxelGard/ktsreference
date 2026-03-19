

# contentEquals

Checks if the two specified arrays are structurally equal to one another.

```kotlin
@ExperimentalUnsignedTypesinfix fun UIntArray?.contentEquals(other: UIntArray?): Boolean(source)
```

```kotlin
import kotlin.experimental.ExperimentalUnsignedTypes

@ExperimentalUnsignedTypes
fun main() {
    val first: UIntArray? = uintArrayOf(1u, 2u, 3u)
    val second: UIntArray? = uintArrayOf(1u, 2u, 3u)
    val third: UIntArray?  = uintArrayOf(4u, 5u)

    println(first contentEquals second)   // true
    println(first contentEquals third)    // false
    println(first contentEquals null)     // false
    println(null contentEquals null)      // true
}
```


[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/content-equals.html)

    