

# contentHashCode

Returns a hash code based on the contents of this array as if it is List.

```kotlin
@ExperimentalUnsignedTypesfun UIntArray?.contentHashCode(): Int(source)
```

```kotlin
import kotlin.experimental.*

@OptIn(ExperimentalUnsignedTypes::class)
fun main() {
    // Create a UIntArray
    val numbers: UIntArray? = uintArrayOf(10u, 20u, 30u)

    // Get a hash code based on its contents
    val hash = numbers.contentHashCode()

    println("Hash code: $hash")   // prints the hash code of the array
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/content-hash-code.html)

    