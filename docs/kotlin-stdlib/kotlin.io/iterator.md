

# iterator

Returns an Iterator of bytes read from this input stream.

```kotlin
operator fun BufferedInputStream.iterator(): ByteIterator(source)
```

```kotlin
import java.io.BufferedInputStream
import java.io.ByteArrayInputStream

fun main() {
    val text = "Hello, Kotlin!"
    val bis = BufferedInputStream(ByteArrayInputStream(text.toByteArray()))

    for (b in bis) {                // Uses BufferedInputStream.iterator()
        print(b.toInt().toChar())    // Convert byte to char for display
    }
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.io/iterator.html)

    