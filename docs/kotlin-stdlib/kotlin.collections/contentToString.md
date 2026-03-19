

# contentToString

Returns a string representation of the contents of the specified array as if it is List.

```kotlin
@ExperimentalUnsignedTypesfun UIntArray?.contentToString(): String(source)
```

```kotlin
@ExperimentalUnsignedTypes
fun main() {
    val numbers: UIntArray? = uintArrayOf(10u, 20u, 30u)
    println(numbers.contentToString())   // prints: [10, 20, 30]

    val empty: UIntArray? = null
    println(empty.contentToString())      // prints: null
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/content-to-string.html)

    