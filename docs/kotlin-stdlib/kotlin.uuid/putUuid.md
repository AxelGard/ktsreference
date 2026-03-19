

# putUuid

Writes the specified uuid value at this buffer's current position.

```kotlin
@ExperimentalUuidApi@IgnorableReturnValuefun ByteBuffer.putUuid(uuid: Uuid): ByteBuffer(source)
```

```kotlin
import java.nio.ByteBuffer
import kotlin.uuid.ExperimentalUuidApi
import kotlin.uuid.Uuid

@OptIn(ExperimentalUuidApi::class)
fun main() {
    val buffer = ByteBuffer.allocate(16)
    val uuid = Uuid.random()

    // Write the UUID into the buffer at the current position
    buffer.putUuid(uuid)

    // Prepare the buffer for reading
    buffer.flip()

    // Read the UUID back from the buffer
    val readUuid = buffer.getUuid()

    println("Original UUID: $uuid")
    println("Read UUID    : $readUuid")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.uuid/put-uuid.html)

    