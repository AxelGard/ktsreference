

# immutableBlobOf

Warning since 1.9

```kotlin
external fun immutableBlobOf(vararg elements: Short): ImmutableBlob(source)
```

```kotlin
import kotlin.native.ImmutableBlob
import kotlin.native.immutableBlobOf

fun main() {
    // Create an immutable blob from a list of Short values
    val blob: ImmutableBlob = immutableBlobOf(10, 20, 30, 40, 50)

    // Access the size of the blob
    println("Blob size: ${blob.size}")

    // Read and print each element
    for (index in 0 until blob.size) {
        println("Element $index: ${blob[index]}")
    }
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.native/immutable-blob-of.html)

    