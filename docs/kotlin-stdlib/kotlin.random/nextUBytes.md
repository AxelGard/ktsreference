

# nextUBytes

Fills the specified unsigned byte array with random bytes and returns it.

```kotlin
@ExperimentalUnsignedTypes@IgnorableReturnValuefun Random.nextUBytes(array: UByteArray): UByteArray(source)
```

```kotlin
import kotlin.random.Random
import kotlin.experimental.ExperimentalUnsignedTypes

@OptIn(ExperimentalUnsignedTypes::class)
fun main() {
    val bytes = UByteArray(10)
    Random.nextUBytes(bytes)
    println(bytes.joinToString(", ") { it.toString() })
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.random/next-u-bytes.html)

    