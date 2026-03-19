

# DEFAULT_BUFFER_SIZE

Returns the default buffer size when working with buffered streams.

```kotlin
const val DEFAULT_BUFFER_SIZE: Int(source)
```

```kotlin
import kotlin.io.DEFAULT_BUFFER_SIZE
import java.io.FileInputStream

fun readFileInChunks(filePath: String) {
    FileInputStream(filePath).use { fis ->
        val buffer = ByteArray(DEFAULT_BUFFER_SIZE)
        var bytesRead: Int
        while (fis.read(buffer).also { bytesRead = it } != -1) {
            // Process `buffer` up to `bytesRead` bytes
        }
    }
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.io/-d-e-f-a-u-l-t_-b-u-f-f-e-r_-s-i-z-e.html)

    