

# getUuid

Reads a Uuid value at this buffer's current position.

```kotlin
@ExperimentalUuidApifun ByteBuffer.getUuid(): Uuid(source)
```

```kotlin
import java.nio.ByteBuffer
import java.util.UUID
import kotlin.uuid.ExperimentalUuidApi
import kotlin.uuid.Uuid

@ExperimentalUuidApi
fun main() {
    // Generate a random UUID
    val original = UUID.randomUUID()

    // Write the UUID into a ByteBuffer (16 bytes)
    val buffer = ByteBuffer.allocate(16)
    buffer.putLong(original.mostSignificantBits)
    buffer.putLong(original.leastSignificantBits)

    // Prepare buffer for reading
    buffer.flip()

    // Read the UUID back from the buffer
    val uuid = buffer.getUuid()

    println("Original UUID: $original")
    println("Read UUID:     $uuid")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.uuid/get-uuid.html)

    